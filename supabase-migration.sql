-- HypeShow — Conversations Table
-- Run this ONCE in Supabase Dashboard → SQL Editor

CREATE TABLE IF NOT EXISTS conversations (
  id           uuid        DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id      text        NOT NULL,
  officer_id   text        NOT NULL,
  date         text        NOT NULL,
  local_key    text        UNIQUE,
  mode         text        DEFAULT '1on1',
  officer_name text,
  officer_role text,
  history      jsonb       DEFAULT '[]',
  summary      text,
  msg_count    integer     DEFAULT 0,
  updated_at   timestamptz DEFAULT now(),
  created_at   timestamptz DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_conv_user_time
  ON conversations(user_id, updated_at DESC);

ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;

-- Temporary: open access (tighten after Google Auth)
CREATE POLICY "allow_anon_access"
  ON conversations FOR ALL USING (true);
