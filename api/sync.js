export const config = { runtime: 'edge' };

export default async function handler(req) {
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405 });
  }

  const SUPABASE_URL = process.env.SUPABASE_URL;
  const SERVICE_KEY  = process.env.SUPABASE_KEY;

  if (!SUPABASE_URL || !SERVICE_KEY) {
    return new Response(JSON.stringify({ error: 'Supabase not configured' }), { status: 500 });
  }

  const body = await req.json();
  const { action, userId } = body;

  if (!userId) {
    return new Response(JSON.stringify({ error: 'userId required' }), { status: 400 });
  }

  const sbHeaders = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${SERVICE_KEY}`,
    'apikey': SERVICE_KEY,
  };

  // ── PUSH: upsert one conversation record ──────────────────────────────────
  if (action === 'push') {
    const { conversation } = body;
    if (!conversation) {
      return new Response(JSON.stringify({ error: 'conversation required' }), { status: 400 });
    }

    const payload = {
      user_id:      userId,
      officer_id:   conversation.officer_id,
      date:         conversation.date,
      local_key:    conversation.local_key,
      mode:         conversation.mode || '1on1',
      officer_name: conversation.officer_name || null,
      officer_role: conversation.officer_role || null,
      history:      conversation.history || [],
      summary:      conversation.summary || null,
      msg_count:    (conversation.history || []).length,
      updated_at:   new Date().toISOString(),
    };

    const res = await fetch(`${SUPABASE_URL}/rest/v1/conversations`, {
      method: 'POST',
      headers: {
        ...sbHeaders,
        'Prefer': 'resolution=merge-duplicates,return=minimal',
      },
      body: JSON.stringify(payload),
    });

    const text = res.ok ? '' : await res.text();
    return new Response(
      JSON.stringify({ ok: res.ok, status: res.status, detail: text }),
      { headers: { 'Content-Type': 'application/json' } }
    );
  }

  // ── PULL: latest 50 conversations for this user ───────────────────────────
  if (action === 'pull') {
    const res = await fetch(
      `${SUPABASE_URL}/rest/v1/conversations?user_id=eq.${encodeURIComponent(userId)}&order=updated_at.desc&limit=50`,
      { headers: sbHeaders }
    );

    if (!res.ok) {
      const err = await res.text();
      return new Response(JSON.stringify({ error: 'pull failed', detail: err }), { status: 500 });
    }

    const data = await res.json();
    return new Response(
      JSON.stringify({ conversations: data }),
      { headers: { 'Content-Type': 'application/json' } }
    );
  }

  return new Response(JSON.stringify({ error: 'unknown action' }), { status: 400 });
}
