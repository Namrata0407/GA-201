import React, { useState, useEffect } from 'react';
import {
  Box,
  Grid,
  GridItem,
  Heading,
  Text,
  Stack,
  Divider,
} from '@chakra-ui/react';

const OrderPage = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // Fetch orders data from the backend or API
    // Replace the placeholder API URL with your actual backend URL
    fetch('http://localhost:5000/orders')
      .then((response) => response.json())
      .then((data) => setOrders(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <Box p={4}>
      <Heading as="h1" mb={8} textAlign="center">
        Orders
      </Heading>
      <Grid templateColumns="repeat(4, 1fr)" gap={8}>
        {Object.values(orders).map((order) => (
          <GridItem key={order.order_id}>
            <Box
              borderWidth="1px"
              borderRadius="lg"
              overflow="hidden"
              boxShadow="md"
              transition="transform 0.3s"
              _hover={{ transform: 'translateY(-5px)' }}
            >
              <Box p={6}>
                <Stack spacing={3}>
                  <Heading as="h2" size="md">
                    Order ID: {order.order_id}
                  </Heading>
                  <Text>Customer: {order.customer_name}</Text>
                  <Text>Status: {order.status}</Text>
                  <Text fontWeight="bold">Dishes:</Text>
                  {order.dishes.map((dish) => (
                    <Text key={dish.dish_id}>
                      - {dish.dish_name} (${dish.price})
                    </Text>
                  ))}
                </Stack>
                <Divider mt={6} />
              </Box>
            </Box>
          </GridItem>
        ))}
      </Grid>
    </Box>
  );
};

export default OrderPage;
