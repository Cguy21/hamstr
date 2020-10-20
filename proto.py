from datetime import datetime, timedelta, time

mollie = Service(
    'https://api.mollie.com/v2/',
    api_key='123',
)

# pydantic
class Payment(Model):
    resource: str
    id: str
    mode: str
    created_at: datetime
    status: str


@mollie.collector(Payment, interval=timedelta(days=1), start=time(hour=17))
def daily_payments():
    last_id = mollie.ctx.get('last_id')
    resp = mollie.get('payments/', params={'from': last_id})
    payments = resp.json()['_embedded']
    mollie.ctx['last_id'] = payments[-1].id
    # will serialize payments into `Payment` objects
    # and store these in the nosql database
    return payments


app = Stoord()  # fastapi wrapper
app.add_service(mollie)

app.run_collectors()  # manually run all collectors
