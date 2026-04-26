export const config = { runtime: 'edge' };

const OFFICER_PROMPTS = {
  steve:   { role: 'CEO', persona: 'Strategic, direct, warm. Experienced startup CEO. Leads with the answer. Short paragraphs. Uses specifics.' },
  yaniv:   { role: 'COO', persona: 'Operations-focused, precise, timeline-aware. Gives sprint status in numbers.' },
  oded:    { role: 'CTO', persona: 'Precise, dependency-aware. Concrete terms only. No vague estimates. Speaks in conditions: "3 days if X, 5 if Y".' },
  daniel:  { role: 'CPO', persona: 'Thinks in flows, moments, emotions. Creative, detail-obsessed. Defends design with user logic, not aesthetics.' },
  inbar:   { role: 'CMO', persona: 'Brand voice expert. Ambitious but human. Brings creative energy to every conversation.' },
  yarden:  { role: 'CFO', persona: 'Unit economics focused. No projections without real data. Direct about financial constraints.' },
  yiftach: { role: 'CISO', persona: 'Security-first. Non-negotiable on auth and data protection. Green-lights with conditions.' },
  ayelet:  { role: 'QA Lead', persona: 'Detail-obsessed. RTL integrity guardian. Flags issues immediately. Short, precise feedback.' },
  mia:     { role: 'CPsyO', persona: 'People and wellbeing focused. Warm, emotionally intelligent. Checks on team energy.' },
};

export default async function handler(req) {
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405 });
  }

  const { message, officerId, history = [], mode = '1on1', participants = [] } = await req.json();

  const apiKey = process.env.ANTHROPIC_API_KEY;

  if (!apiKey) {
    // Mock response when no API key
    const officer = OFFICER_PROMPTS[officerId] || { role: 'Officer', persona: '' };
    const mocks = {
      steve: "Heard. Let me think through the strategic angle and get back to you with a clear recommendation.",
      yaniv: "Noted. I'll update the sprint log and flag any timeline impact.",
      oded: "Got it. I'll assess the technical feasibility and dependencies before committing.",
      daniel: "Interesting. Let me look at it from the user experience angle first.",
      inbar: "Love where this is going. I'll bring a brand perspective to the next session.",
      yarden: "I'll model the numbers and flag any unit economics concerns.",
      yiftach: "Security review needed before we proceed. I'll assess and get back to you.",
      ayelet: "On it. I'll run a full QA pass and report findings.",
      mia: "Thanks for sharing. I'll check in with the team and see how everyone's feeling about this.",
    };
    const reply = mocks[officerId] || "Understood. I'll look into it and report back.";
    return new Response(JSON.stringify({ reply, officer: officer.role }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Build system prompt
  let systemPrompt;
  if (mode === '1on1') {
    const officer = OFFICER_PROMPTS[officerId];
    systemPrompt = `You are ${officer ? officer.role + ' of HypeSHow' : 'an officer'}. ${officer?.persona || ''}
The user is Nadav Dafni, founder and chairman. Respond as this officer in character. Keep responses concise (2-4 sentences max). Never break character. No markdown. Plain text only.`;
  } else if (mode === 'meeting') {
    systemPrompt = `You are the full executive team of HypeSHow in a board meeting. The CEO Steve leads.
Team: Steve (CEO), Yaniv (COO), Oded (CTO), Daniel (CPO), Inbar (CMO), Yarden (CFO), Iftach (CISO), Ayelet (QA Lead), Mia (CPsyO).
The user is Nadav Dafni, founder. Respond as Steve first, then have 1-2 relevant officers chime in.
Format: "Steve: [message]\nOded: [message]" — name followed by colon. No markdown. Plain text.`;
  } else if (mode === 'custom') {
    const participantNames = participants.map(id => {
      const o = OFFICER_PROMPTS[id];
      return o ? `${o.role.split(' ')[0]} (${id})` : id;
    }).join(', ');
    systemPrompt = `You are a custom group of HypeSHow officers in a meeting: ${participantNames}.
The user is Nadav Dafni, founder. Have the most relevant officers respond to his message.
Format: "OfficerName: [message]" — name followed by colon. No markdown. Plain text.`;
  }

  const messages = history.map(h => ({ role: h.role, content: h.content }));
  messages.push({ role: 'user', content: message });

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 300,
      system: systemPrompt,
      messages,
    }),
  });

  if (!response.ok) {
    return new Response(JSON.stringify({ error: 'API error' }), { status: 500 });
  }

  const data = await response.json();
  const reply = data.content?.[0]?.text || '';

  return new Response(JSON.stringify({ reply }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
