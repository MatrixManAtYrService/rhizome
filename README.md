[![Test](https://github.corp.clover.com/matt-rixman/rhizome/workflows/Test/badge.svg)](https://github.corp.clover.com/matt-rixman/rhizome/actions/workflows/test.yml) \[[docs](https://github.corp.clover.com/pages/matt-rixman/rhizome/)\]

# Trifolium

Two species of clover, with different ways of propagating:

- *Trifolium repens* is a species of flowering clover which repoduces in the normal way (bees, pollen, etc) but which also reproduces asexually via **stolons**.
- *Trifolium ambiguum* is also a species clover, also with a typical flowering reproductive cycle, but it's mode of asexual reproduction involves **rhizomes**.

Rhizomes and stolons are similar in that they grow out horizontally from one clover and connect it to other nearby clover.
They're different in that rhizomes do this underground (another plant that does this is hops 🍺), and stolons do this aboveground (strawberries also do this 🍓).

This project provides two python packages:

- `stolon` is a data access layer for any locally-attached devices and for Clover's http API's.
- `rhizome` is a data access layer for clover's databases

## As a Repository for Tribal Knowledge

If you want to access clover databases, there are a variety of questions you might ask:

- do I need to forward a port anywhere?
- what host should I talk to?
- what user/pass should I use
- what columns/attributes are available?
- should I expect certain environments to differ from others?

There are a variety of similar questions that you might ask if you're working with a Clover device or with Clover API's

- how do I get a token?
- which API should I use for some action or another?
- how do I reconfigure my device in some way or another?

This project aims to capture the answers to these questions in code.
The goal is that trifolium users can focus on business/test logic instead, since trifolium itself knows how to do these things.

## Local Servers

Trifolium also aims to separate the "business logic" of a test from the complexities of data access or API usage.
This is valuable because it makes either side of the problem simpler, and also because it will allow us to run the "same test" both locally and in situations where the data access methods are different (such as in retool).

In the local mode it requires that two servers be running.
To start these, run `rhizome serve` and `stolon serve`.

Then you can run code like this:

```python3
from sqlmodel import select
from rhizome.client import RhizomeClient
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from stolon.client import StolonClient
from trifolium.environments import dev

# having an object for the "environment" enables dependency injection
# this makes for code that's easier to share
environment = dev.Environment(
    rhizome_client=RhizomeClient(data_in_logs=False),
    stolon_client=StolonClient(data_in_logs=False)
)
merchant_uuid = "ABC123DEF4567"

merchant_detail = environment.db.billing_bookkeeper.select_first(
    select(DevBillingBookkeeper.MerchantDetail)
    .join(DevBillingBookkeeper.BillingEntity)
    .where(DevBillingBookkeeper.BillingEntity.entity_uuid == merchant_uuid)
    # if entity_uuid weren't a valid column in dev, this would fail during type-checking
    # also, you can tab-complete it (unlike string full of SQL)
)

if merchant_detail:
    print(f"Merchant {merchant_uuid} exists in billing system")
else:
    # this helper function uses a client generated from the agreement service's openapi spec
    # if the endpoint changed in a way that causes a problem for our test,
    # that breakage would show up in your editor as a type error
    acceptance = environment.api.agreement.ensure_merchant_acceptance(
        merchant_uuid=merchant_uuid,
        account_uuid="XYZ789GHI0123",
        agreement_type="BILLING",
    )
    print(f"Created billing acceptance: {acceptance.id}")
```

If you have a `rhizome` or `stolon` server running, it will handle the "tribal knowledge" part.
It connects to the right servers, forwards the right ports, and summons the right credentials.
Sometimes it'll need you to log in on its behalf so that it can get a session token or the correct credientials.

Since the server is running in a separate terminal, there is a dedicated place for informing you what's being done on your behalf.
Debugging things like authentication or flaky servers happens within the server.
This keeps the test logic simple and easy to read.

## Env-specific Types

Whevever possible, references are type hinted and those types are environment specific.
This is made possible by a variety of sync commands:

- `rhizome sync schema` queries environment databases and generates files like [billing_app_suppression.sql](./src/rhizome/environments/dev/expected_data/billing_app_suppression.sql) which are then used to generate files like [app_suppression.py](src/rhizome/models/billing/app_suppression.py)
`rhizome sync data` queries environment databases and generates files like [billing_bookkeeper_tier_detail.json]( src/rhizome/environments/dev/expected_data/billing_bookkeeper_tier_detail.json) which are used by [test_environment_access.py](tests/test_environment_access.py) to ensure that the above models are correct for that environment.
`stolon sync spec` requests openapi specs generates http clients in directories like [src/stolon/generated/billing_bookkeeper_dev](src/stolon/generated/billing_bookkeeper_dev)

This means that--supposing the syncs were run recently--the types are representative of what you'll actually find in those environments.
So if you have a test that will succeed in dev but will error in demo due to environment differences there's chance that a type checker can find those problems for you in seconds rather than finding them later on when you actually run the code.

This is handy for catching bugs early, but it also enables LSP-enabled editors to provide tab completion and enhanced navigation (unlike strings containing SQL queries).
Lastly, You can use an LSP-MCP bridge like [serena](https://github.com/oraios/serena) to give AI agents a way to explore the synced types--the added context improves their ability to reason about our data landscape.
