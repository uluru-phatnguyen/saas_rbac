import unittest
import base_test
import json

class RoleClaimTest(base_test.BaseTest):
    def setUp(self):
        super(RoleClaimTest, self).setUp()
        self._org = self.post('/api/orgs', {"name":"claim_org", "url":"https://myorg.com"})
        self._realm = self.post('/api/realms', {"id":"resource_realm"})
        self._role = self.post('/api/orgs/%s/roles' % self._org["id"], {"name":"my_role", "organization_id":self._org["id"], "realm_id":self._realm["id"]})
        self._license = self.post('/api/orgs/%s/licenses' % self._org["id"], {"name":"my_license", "organization_id":self._org["id"], "effective_at": "2019-01-01T00:00:00", "expired_at": "2030-01-01T00:00:00"})
        self._resource = self.post('/api/realms/%s/resources' % self._realm["id"], {"resource_name":"my_resource", "realm_id":self._realm["id"]})


    def tearDown(self):
        self.delete('/api/realms/%s/resources/%s/claims/%s' % (self._realm["id"], self._resource["id"], self._claim["id"]))
        self.delete('/api/orgs/%s/licenses/%s' % (self._org["id"], self._license["id"]))
        self.delete('/api/realms/%s/resources/%s' % (self._realm["id"], self._resource["id"]))
        self.delete('/api/orgs/%s/roles/%s' % (self._org["id"], self._role["id"]))
        self.delete('/api/realms/%s' % self._realm["id"])
        self.delete('/api/orgs/%s' % self._org["id"])

    def test_add_remove_claim_to_role(self):
        self._claim = self.post('/api/realms/%s/resources/%s/claims' % (self._realm["id"], self._resource["id"]), {"action":"READ", "realm_id":self._realm["id"]})
        self.assertEquals("READ", self._claim["action"])
        #
        resp = self.put('/api/realms/%s/resources/%s/claims/%s/roles/%s' % (self._realm["id"], self._resource["id"], self._claim["id"], self._role["id"]), {})
        self.assertEquals(1, resp, json.dumps(resp))
        resp = self.delete('/api/realms/%s/resources/%s/claims/%s/roles/%s' % (self._realm["id"], self._resource["id"], self._claim["id"], self._role["id"]))
        self.assertEquals(1, resp, json.dumps(resp))

if __name__ == '__main__':
    unittest.main()
