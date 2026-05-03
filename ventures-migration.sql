-- HypeShow — Ventures Table (Schema v1.0)
-- 16 fields | Approved: 2026-04-30
-- Run in Supabase Dashboard → SQL Editor

CREATE TYPE target_audience_enum AS ENUM ('SMB', 'Enterprise', 'Consumer');
CREATE TYPE funding_stage_enum AS ENUM ('Seed', 'Series-A', 'Series-B', 'Growth');
CREATE TYPE business_model_enum AS ENUM ('SaaS', 'B2B', 'B2C', 'Marketplace', 'Fintech', 'Other');
CREATE TYPE primary_challenge_enum AS ENUM ('Fundraising', 'Product_Launch', 'Customer_Acquisition', 'Scalability', 'Strategy');
CREATE TYPE target_geo_enum AS ENUM ('Global', 'US', 'Europe', 'Israel', 'Asia');
CREATE TYPE product_stage_enum AS ENUM ('Concept', 'Prototype', 'MVP', 'Revenue_Generating', 'Scaling');
CREATE TYPE revenue_model_enum AS ENUM ('Subscription', 'Transactional', 'Ad-based', 'Licensing', 'Freemium');
CREATE TYPE brand_voice_enum AS ENUM ('Professional', 'Disruptive', 'Bold', 'Trustworthy', 'Friendly');
CREATE TYPE team_size_enum AS ENUM ('Solo_Founder', '2-5', '6-15', '16-50', '50+');
CREATE TYPE industry_category_enum AS ENUM (
  'Cybersecurity', 'AI/ML', 'FinTech', 'HealthTech', 'E-commerce',
  'Cloud Infrastructure', 'SaaS', 'EdTech', 'Blockchain/Web3',
  'MarketplacesTech', 'IoT', 'Biotech', 'CleanTech', 'InsurTech',
  'Supply Chain', 'Logistics', 'HR/Recruiting', 'Travel/Hospitality',
  'Media/Entertainment', 'Other'
);

CREATE TABLE IF NOT EXISTS ventures (
  id                uuid                  DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id           text                  NOT NULL,

  -- Step 1: Identity
  company_name      varchar(100)          NOT NULL,
  pitch             varchar(500)          NOT NULL,
  target_audience   target_audience_enum  NOT NULL,
  team_size         team_size_enum        NOT NULL,

  -- Step 2: Business Model
  business_model    business_model_enum   NOT NULL,
  revenue_model     revenue_model_enum    NOT NULL,
  product_stage     product_stage_enum    NOT NULL,
  funding_stage     funding_stage_enum    NOT NULL,
  tech_stack        varchar(200),

  -- Step 3: Strategy
  primary_challenge primary_challenge_enum NOT NULL,
  immediate_goal    varchar(300)           NOT NULL,
  unique_value_prop varchar(150)           NOT NULL,
  competitors       varchar(250),
  target_geo        target_geo_enum        NOT NULL,

  -- Step 4: Brand
  industry_category industry_category_enum NOT NULL,
  brand_voice       brand_voice_enum        NOT NULL,

  -- Meta
  created_at        timestamptz            DEFAULT now(),
  updated_at        timestamptz            DEFAULT now()
);

-- Index for fast user lookups
CREATE INDEX IF NOT EXISTS idx_ventures_user
  ON ventures(user_id, updated_at DESC);

-- RLS
ALTER TABLE ventures ENABLE ROW LEVEL SECURITY;

CREATE POLICY "users_own_ventures"
  ON ventures FOR ALL
  USING (user_id = current_setting('request.jwt.claims', true)::json->>'sub');

-- Auto-update timestamp
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = now(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER ventures_updated_at
  BEFORE UPDATE ON ventures
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
