import asyncio
import random
class payment:
    def __init__(self,):
        self.lock = asyncio.Lock()
        self.orders ={}
        self.stock = 5
        self.users = {}
    async def process_payment(self,user_id):
        async with self.lock:
            if self.stock > 0:
                self.stock -= 1
                order_id = f"ord{random.randint(1000,9999)}-{user_id}"
                # print("order_id",order_id)
                self.orders[order_id] = {"status":"process"}
                await self.payment_gateway(user_id,order_id)
            else:
                await self.payment_failed(user_id)
    async def payment_gateway(self,user_id,order_id):
        print("payment processing: ",user_id)
        await asyncio.sleep(random.uniform(1, 3))
        await self.payment_webhook(order_id)
    async def payment_webhook(self,order_id):
        self.orders[order_id]["status"] = "Paid"
        print(f"order confirmed your order id {order_id}")
    async def payment_failed(self,user_id):
        self.users[user_id] = "payment_failed"
        print("less stack")

async def main():
    pay = payment()
    tasks = [pay.process_payment(i) for i in [123,234,45,56,90,567]]
    await asyncio.gather(*tasks)
asyncio.run(main())
            
            
            