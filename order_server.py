from concurrent import futures
import time
import grpc
import order_pb2
import order_pb2_grpc

class RestaurantModel():
    def __init__(self):
        self.price = 0

    def get(self, restaurantid):
        if restaurantid == 100:
            self.name = 'ABC Restaurant'
            return self

    def buy(self, menuItemId, quantity):
        if menuItemId == 14:
            cost = 100
        elif menuItemId == 17:
            cost = 200
        self.price += cost * quantity

    def purchase(self):
        return self.price

class ConsumerModel():
    def __init__(self):
        pass

    def get(self, consumerid):
        if consumerid == 101:
            self.name = 'Dave'
            return self

class OrderService(order_pb2_grpc.OrderService):
    def createOrder(self, request, context):
        restaurant = RestaurantModel().get(request.restaurantId)
        consumer = ConsumerModel().get(request.consumerId)
        
        for menuItem in request.lineItems:
            restaurant.buy(menuItem.menuItemId, menuItem.quantity)
        
        price = restaurant.purchase()
        return order_pb2.CreateOrderReply(
            restaurantName=restaurant.name,
            consumerName=consumer.name,
            price=price
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('localhost:12345')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
