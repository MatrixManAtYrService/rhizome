[![Test](https://github.com/MatrixManAtYrService/hello-template/workflows/Test/badge.svg)](https://github.com/MatrixManAtYrService/hello-template/actions/workflows/test.yml) \[[docs](https://matrixmanatyrservice.github.io/hello-template/hello.html)\]

Rhizome is a db access helper for Clover apps.
With it, you can write apps that do this:

```python3
from sqlmodel import Field, Session, SQLModel, create_engine, select
from rhizome.models.bookeeper import fee_summary
import rhizome as r


# forward ports and checkout credentials
handle = r.environments.na_prod.bookeeper.get_handle()

engine = create_engine(handle.connection_string)
with Session(engine) as session:

  # contains models for each table
  FS = r.models.bookkeeper.FeeSummary
  statement = select(FS).where(FS.billing_entity_uuid="JW8H2B9BT6B11R2HHXY3HYQCN6")

  # the modles have per-table sanitization functions
  fs = r.sanitize(session.exec(statement).first())
  print(fs.fee_code)
```

You'll need to have the rhizome server running in order to use any apps that use the rhizome client, just run `rhizome` and leave the terminal open.
```
$ rhizome
rhizome is waiting for connections.
```

As you use apps that import rhizome, this you'll get feedback in this terminal.
```
$ rhizome
rhizome is waiting for clients
Forwarding clover-prod-databases:us-central1:billing-bookkeeper to local port 51234
  kubectl:   Starting proxy for connectionName 'clover-prod-databases:us-central1:billing-bookkeeper' on port '62956' with health check port on '61801'
  kubectl:     2025/08/14 21:28:36 Listening on 127.0.0.1:62956 for clover-prod-databases:us-central1:billing-bookkeeper
  kubectl:     2025/08/14 21:28:36 Ready for new connections
  kubectl:   Forwarding localhost:51234 to remote port 62956...
  kubectl:   Forwarding from 127.0.0.1:51234 -> 62956
  kubectl:   Forwarding from [::1]:51234 -> 62956
Fetching 1password/EventBillingROCred
Checking out britive/Resources/COS-RO-USProd/COS-RO-USProd-profile
  kubectl:   Handling connection for 51234
```



