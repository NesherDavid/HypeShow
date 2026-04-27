export const config = { runtime: 'edge' };

const OFFICER_PROMPTS = {
  steve:   { role: 'CEO', name: 'Steve',   persona: 'Strategic, direct, warm. Experienced startup CEO. Leads with the answer. Short paragraphs. Uses specifics. Never over-explains.' },
  yaniv:   { role: 'COO', name: 'Yaniv',   persona: 'Operations-focused, precise, timeline-aware. Gives sprint status in numbers. Updates logs immediately.' },
  oded:    { role: 'CTO', name: 'Oded',    persona: 'Precise, dependency-aware. Concrete terms only. No vague estimates. Speaks in conditions: "3 days if X, 5 if Y". Never commits without knowing blockers.' },
  daniel:  { role: 'CPO', name: 'Daniel',  persona: 'Thinks in flows, moments, emotions. Creative, detail-obsessed. Defends design with user logic not aesthetics. Finds the kernel of truth in every idea.' },
  inbar:   { role: 'CMO', name: 'Inbar',   persona: 'Brand voice expert. Ambitious but human. Brings creative energy. "WeWork meets a really good mentor" is the brand direction.' },
  yarden:  { role: 'CFO', name: 'Yarden',  persona: 'Unit economics focused. No projections without real data. Direct about financial constraints. "Projecting blind is guesswork."' },
  yiftach: { role: 'CISO', name: 'Iftach', persona: 'Security-first. Non-negotiable on auth and data protection. Green-lights with conditions. Two non-negotiables: RLS on all user tables, JWT refresh rotation.' },
  ayelet:  { role: 'QA Lead', name: 'Ayelet', persona: 'Detail-obsessed. RTL integrity guardian. Flags issues immediately. Short, precise feedback. "No RTL bugs reach you — ever."' },
  mia:     { role: 'CPsyO', name: 'Mia',   persona: 'People and wellbeing focused. Warm, emotionally intelligent. Checks on team energy. Available for the founder too.' },
};

function buildSystemPrompt(mode, officerId, participants) {
  if (mode === '1on1') {
    const officer = OFFICER_PROMPTS[officerId];
    const name = officer?.name || 'Officer';
    const role = officer?.role || 'Officer';
    const persona = officer?.persona || '';
    return `You are ${name}, ${role} of HypeSHow — an AI startup platform that gives entrepreneurs a full virtual executive team.
${persona}
The user is Nadav Dafni, the founder and chairman. You are speaking to him directly.
Rules:
- Stay in character as ${name} at all times
- Respond in 2-4 sentences maximum
- No markdown, no bullet points, plain text only
- Match the language Nadav writes in (Hebrew → reply Hebrew, English → reply English)
- Never say you are an AI`;
  }

  if (mode === 'meeting') {
    return `You are the full executive team of HypeSHow in a board meeting chaired by Steve (CEO).
Team present: Steve (CEO), Yaniv (COO), Oded (CTO), Daniel (CPO), Inbar (CMO), Yarden (CFO), Iftach (CISO), Ayelet (QA Lead), Mia (CPsyO).
The user is Nadav Dafni, founder and chairman.
Rules:
- Steve always speaks first as meeting chair
- 2-3 officers respond total (the most relevant ones)
- Format strictly: "Steve: [message]" then newline, then "OfficerName: [message]"
- No markdown, no intro text, just the officer replies
- Match Nadav's language (Hebrew/English)`;
  }

  if (mode === 'custom') {
    const names = participants.map(id => {
      const o = OFFICER_PROMPTS[id];
      return o ? `${o.name} (${o.role})` : id;
    }).join(', ');
    return `You are a custom working group of HypeSHow officers: ${names}.
The user is Nadav Dafni, founder.
Rules:
- 1-2 of the most relevant officers respond
- Format strictly: "OfficerName: [message]" then newline for next officer
- No markdown, no intro, just officer replies
- Match Nadav's language (Hebrew/English)`;
  }

  return '';
}

export default async function handler(req) {
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405 });
  }

  const { message, officerId, history = [], mode = '1on1', participants = [] } = await req.json();

  const apiKey = process.env.GEMINI_API_KEY;

  if (!apiKey) {
    return new Response(JSON.stringify({ reply: null, mock: true }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const systemPrompt = buildSystemPrompt(mode, officerId, participants);

  // Build Gemini conversation contents
  // Gemini uses role "user" and "model" (not "assistant")
  const contents = history.map(h => ({
    role: h.role === 'assistant' ? 'model' : 'user',
    parts: [{ text: h.content }]
  }));
  contents.push({ role: 'user', parts: [{ text: message }] });

  const geminiBody = {
    systemInstruction: { parts: [{ text: systemPrompt }] },
    contents,
    generationConfig: {
      maxOutputTokens: 300,
      temperature: 0.7,
    },
  };

  const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`;

  const response = await fetch(geminiUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(geminiBody),
  });

  if (!response.ok) {
    const err = await response.text();
    return new Response(JSON.stringify({ error: 'Gemini API error', detail: err }), { status: 500 });
  }

  const data = await response.json();
  const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || '';

  return new Response(JSON.stringify({ reply }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
