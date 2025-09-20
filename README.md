[![Test](https://github.corp.clover.com/matt-rixman/rhizome/workflows/Test/badge.svg)](https://github.corp.clover.com/matt-rixman/rhizome/actions/workflows/test.yml) \[[docs](https://github.corp.clover.com/pages/matt-rixman/rhizome/)\]

# Trifolium

Two species of clover, with different ways of propagating:

- *Trifolium repens* is a species of flowering clover which repoduces in the normal way (bees, pollen, etc) but which also reproduces asexually via **stolons**.
- *Trifolium ambiguum* is also a species clover, also with a typical flowering reproductive cycle, but it's mode of asexual reproduction involves **rhizomes**.

Rhizomes and stolons are similar in that they grow out horizontally from one clover and connect it to other nearby clover.
They're different in that rhizomes do this underground (another plant that does this is hops 🍺), and stolons do this aboveground (strawberries also do this 🍓).

`rhizome` is a data access layer for clover's databases, and `stolon` is a data access layer for clover's http API's.

## As a Repository for Tribal Knowledge

If you want to access clover data, there are a variety of questions you might ask:

- do I need to forward a port anywhere?
- what host should I talk to?
- what user/pass should I use
- what columns/attributes are available?
- should I expect certain environments to differ from others?

This project aims to capture the answers to these questions in code.

## Local Servers

Trifolium also aims to separate the "business logic" of a test from the complexities of data access or API usage.
This is valuable because it makes either side of the problem simpler, and also because it will allow us to run the "same test" both locally and in situations where the data access methods are different (such as in retool).

In the local mode it requires that two servers be running.
To start these, run `rhizome serve` and `stolon serve`.

Then you can run code like this:

```python3
from sqlmodel import select
from rhizome.client import RhizomeClient
from rhizome.environments import DevBillingBookkeeper
from rhizome.models.billing_bookkeeper.table_list import BillingBookkeeperTable

db = DevBillingBookkeeper(RhizomeClient(data_in_logs=False))

# Get the correct FeeSummary version for this environment
FeeSummary = db.get_model(BillingBookkeeperTable.fee_summary)

fee_summary = db.select_first(
    select(FeeSummary).where(FeeSummary.id == 30)
)
assert fee_summary # fail if there is no fee summary with id == 30
safe_fee_summary = fee_summary.sanitize()
assert safe_fee_summary.total_period_units == 3
```

If you have a rhizome server running, it will handle the "tribal knowledge" part.
It connects to the right servers, forwards the right ports, and summons the right credentials.
Sometimes it'll need you to log in on its behalf so that it can get a session token or the correct credientials.

Since the server is running in a separate terminal, there is a dedicated place for informing you what's being done on your behalf.
Debugging things like authentication or flaky servers happens within the server.
This keeps the test logic simple and easy to read.

In a place like retool, where tabular data is made available directly by the environment, the rhizome client will handle supplying the corect data for each call.
In this case, it'll be necessary to analyze a local run and extract the queries such that a retool app can be generated which knows which queries should be used where.
This mode is a TODO.

