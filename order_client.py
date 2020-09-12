import grpc

import order_pb2
import order_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:12345')
    stub = order_pb2_grpc.OrderServiceStub(channel)
    response = stub.createOrder(
        order_pb2.CreateOrderRequest(
            restaurantId=100,
            consumerId=101,
            lineItems=[
                order_pb2.LineItem(
                    menuItemId=14,
                    quantity=2
                ),
                order_pb2.LineItem(
                    menuItemId=17,
                    quantity=1
                )
            ]
        )
    )
    print(f'{response.consumerName} buy ${response.price} foods at {response.restaurantName}')

if __name__ == '__main__':
    run()
