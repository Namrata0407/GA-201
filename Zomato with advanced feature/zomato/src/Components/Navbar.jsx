import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Flex, Box, Text, Link, Spacer, Image } from '@chakra-ui/react';

const Navbar = () => {
    const logoUrl = 'https://tse1.mm.bing.net/th?id=OIP.Sa9ZfKEPzreh38i8xrwQJgHaEo&pid=Api&P=0&h=180/50x50.png'; // Replace with the URL of your logo image

  return (
    <Flex as="nav" bg="teal.500" p={4} color="white" alignItems="center">
      <Flex alignItems="center">
        <Image src={logoUrl} alt="Food Logo" boxSize={8} mr={2} />
        <Text fontSize="2xl" fontWeight="bold">
          Zomato Chronicles
        </Text>
      </Flex>
      <Spacer />
      <Flex alignItems="center">
        <Link as={RouterLink} to="/" color="white" mr={4}>
          Home
        </Link>
        <Link as={RouterLink} to="/menu" color="white" mr={4}>
          Menu
        </Link>
        <Link as={RouterLink} to="/take-orders" color="white" mr={4}>
          Take Orders
        </Link>
        <Link as={RouterLink} to="/orders" color="white" mr={4}>
          Orders
        </Link>
        <Link as={RouterLink} to="/exit" color="white">
          Exit
        </Link>
      </Flex>
    </Flex>
  );
};

export default Navbar;
