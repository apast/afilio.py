import requests


class AfilioSalesAPI():
    """
    Sales & Leads endpoint
    http://v2.afilio.com.br/api/leadsale_api.php?
         type=sale|lead
        &mode=list
        &token=<affiliate api token>
        &affid=<affiliate id>
        &dateStart=<filter begin> (format: YYYY-MM-DD)
        &dateEnd=<filter end> (format: YYYY-MM-DD)
        &format=xml|json|csv|rss (default: json)
    """
    LEADS = "lead"
    SALES = "sale"

    def __init__(self, token, affiliate_id):
        self.token = token
        self.affiliate_id = affiliate_id
        self.url_base = "http://v2.afilio.com.br/api/leadsale_api.php"

    def _build_params(self, report_type, date_start, date_end):
        if not report_type in [AfilioSalesAPI.LEADS, AfilioSalesAPI.SALES]:
            raise ValueError("Use one of valid report type: AfilioSalesAPI.LEADS (lead) or AfilioSalesAPI.SALES (sale)")

        params = dict(mode="list",
                      format="json",
                      token=self.token,
                      affid=self.affiliate_id,
                      type=report_type,
                      dateStart=date_start,
                      dateEnd=date_end,
                      )
        return params

    def _load(self, report_type, date_start, date_end):
        params = self._build_params(report_type, date_start, date_end)
        report = requests.get(self.url_base, params=params)
        return report.json()

    def sales(self, date_start, date_end):
        sales = self._load(report_type=AfilioSalesAPI.SALES)
        pass

    def leads(self):
        self._load(report_type=AfilioSalesAPI.LEADS)


import unittest


class AfilioSalesAPITestCase(unittest.TestCase):
    def test_invalid_params(self):
        self.assertRaises(ValueError, AfilioSalesAPI(None, None)._build_params, report_type=None, date_start=None, date_end=None)
        self.assertRaises(ValueError, AfilioSalesAPI(None, None)._build_params, report_type="a", date_start=None, date_end=None)

    def test_lead_request_params(self):
        api = AfilioSalesAPI("token", "affid")
        base_params = dict(affid=api.affiliate_id, token=api.token, format="json", mode="list")

        date_start = "2016-03-01"
        date_end = "2016-03-31"

        expected = {}
        expected.update(base_params)
        expected["type"] = AfilioSalesAPI.LEADS
        expected["dateStart"] = date_start
        expected["dateEnd"] = date_end
        self.assertCountEqual(expected,
                              api._build_params(report_type=AfilioSalesAPI.LEADS, date_start=date_start, date_end=date_end))
