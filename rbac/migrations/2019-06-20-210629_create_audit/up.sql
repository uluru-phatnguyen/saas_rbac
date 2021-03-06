CREATE TABLE IF NOT EXISTS rbac_audit_records (
  id VARCHAR(36) NOT NULL PRIMARY KEY,
  message TEXT NOT NULL,
  action VARCHAR(100),
  context TEXT,
  created_by VARCHAR(36),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
