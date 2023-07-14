import React from 'react';
import { Box, Heading, Text } from '@chakra-ui/react';

const HomePage = () => {
  return (
    <Box textAlign="center">
      <Heading as="h1" mb={4} mt={"150px"} color={"#CA1E2E"}>
        Welcome to Zomato Chronicles!
      </Heading>
      <Text fontSize="xl" color={"#319795"}>
        Discover the great food fiasco and embark on a culinary adventure with Zesty Zomato.
      </Text>
    </Box>
  );
};

export default HomePage;
