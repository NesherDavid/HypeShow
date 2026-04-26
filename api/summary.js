export const config = { runtime: 'edge' };

export default async function handler(req) {
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405 });
  }

  const { history = [], officerName, officerRole, mode = '1on1', participants = [] } = await req.json();

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey || history.length < 2) {
    return new Response(JSON.stringify({ summary: null }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const transcript = history.map(m => {
    const speaker = m.role === 'user' ? 'Nadav' : (officerName || 'Officer');
    return `${speaker}: ${m.content}`;
  }).join('\n');

  const contextDesc = mode === '1on1'
    ? `1-on-1 conversation between Nadav (founder) and ${officerName} (${officerRole})`
    : mode === 'meeting'
    ? 'Full team board meeting with all HypeSHow officers'
    : `Custom working session with: ${participants.join(', ')}`;

  const prompt = `Summarize this ${contextDesc} in 2-3 sentences. Extract: key decisions made, action items, and any blockers mentioned. Write in the same language as the conversation. Be concise and factual.

Transcript:
${transcript}`;

  const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;

  const response = await fetch(geminiUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ role: 'user', parts: [{ text: prompt }] }],
      generationConfig: { maxOutputTokens: 200, temperature: 0.3 },
    }),
  });

  if (!response.ok) {
    return new Response(JSON.stringify({ summary: null }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const data = await response.json();
  const summary = data.candidates?.[0]?.content?.parts?.[0]?.text || null;

  return new Response(JSON.stringify({ summary }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
