=====
Usage
=====

To use py-flowdock in a project::

    import flowdock
    org_name = <org name>
    api_token = <api_token>
    flowdock.Configuration(org_name, (api_token, ""))
    f = flowdock.Flow()
    f.list_flows()