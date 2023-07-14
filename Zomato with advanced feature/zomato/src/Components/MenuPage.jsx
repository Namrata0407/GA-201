

import React, { useState, useEffect } from 'react';
import {
  Box,
  Grid,
  GridItem,
  Heading,
  Text,
  Image,
  Stack,
  Divider,
  Button,
  useDisclosure,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  FormControl,
  FormLabel,
  Input,
  ModalFooter,
  Select,
  IconButton,
  useToast,
} from '@chakra-ui/react';
import { DeleteIcon } from '@chakra-ui/icons';

const MenuPage = () => {
  const [count,setCount] = useState(0)
  const [menu, setMenu] = useState([]);
  const [newMenuItem, setNewMenuItem] = useState({
    dish_name: '',
    price: '',
    availability: 'yes',
  });
  const { isOpen, onOpen, onClose } = useDisclosure();

  const toast = useToast();

  useEffect(() => {
    fetchMenuItems();
  }, [count]);

  const fetchMenuItems = () => {
    fetch('http://localhost:5000/menu')
      .then((response) => response.json())
      .then((data) => setMenu(data))
      .catch((error) => console.error(error));
  };

  const handleAddMenu = () => {
    fetch('http://localhost:5000/menu', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newMenuItem),
    })
      .then((response) => {
        console.log("added");
        return response.json(); // Return the response JSON
      })
      .then((data) => {
        console.log("item added");
        fetchMenuItems();
        onClose(); // Close the modal after adding a new item
      })
      .catch((error) => console.error(error));
  };

  const handleDeleteMenu = (dishId) => {
    fetch(`http://localhost:5000/menu/${dishId}`, {
      method: 'DELETE',
    })
      .then((response) => response.json())
      .then((data) => {
        // console.log("item deleted");
        setCount(count+1)
        // fetchMenuItems();
        toast({
          title: 'Menu Item Deleted',
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      })
      .catch((error) => console.error(error));
  };

  const handleChange = (e) => {
    setNewMenuItem({
      ...newMenuItem,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <Box p={4}>
      <Heading as="h1" mb={8} textAlign="center">
        Menu
      </Heading>
      <Grid templateColumns="repeat(4, 1fr)" gap={8}>
        {menu.map((dish) => (
          <GridItem key={dish.dish_id}>
            <Box
              borderWidth="1px"
              borderRadius="lg"
              overflow="hidden"
              boxShadow="md"
              transition="transform 0.3s"
              _hover={{ transform: 'translateY(-5px)' }}
            >
              <Image
                src={"https://tse4.mm.bing.net/th?id=OIP.eD7MpRmuCp5oKFlcdoKmuwHaE8&pid=Api&P=0&h=180"}
                alt={dish.dish_name}
                m="auto"
                borderRadius="lg"
              />
              <Box p={6}>
                <Stack spacing={3}>
                  <Heading as="h2" size="md">
                    {dish.dish_name}
                  </Heading>
                  <Text>{dish.description}</Text>
                  <Text color="blue.600" fontSize="2xl">
                    ${dish.price}
                  </Text>
                </Stack>
                <Divider mt={6} />
                <IconButton
                  icon={<DeleteIcon />}
                  colorScheme="red"
                  variant="ghost"
                  size="sm"
                  onClick={() => handleDeleteMenu(dish.dish_id)}
                />
              </Box>
            </Box>
          </GridItem>
        ))}
        <GridItem>
          <Box
            borderWidth="1px"
            borderRadius="lg"
            overflow="hidden"
            boxShadow="md"
            transition="transform 0.3s"
            _hover={{ transform: 'translateY(-5px)' }}
            cursor="pointer"
            onClick={onOpen}
          >
            <Box p={6} textAlign="center">
              <Text fontSize="xl" fontWeight="bold">
                Add a Menu
              </Text>
            </Box>
          </Box>
        </GridItem>
      </Grid>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Add a Menu</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <FormControl>
              <FormLabel>Dish Name</FormLabel>
              <Input
                type="text"
                name="dish_name"
                value={newMenuItem.dish_name}
                onChange={handleChange}
              />
            </FormControl>
            <FormControl mt={4}>
              <FormLabel>Price</FormLabel>
              <Input
                type="number"
                name="price"
                value={newMenuItem.price}
                onChange={handleChange}
              />
            </FormControl>
            <FormControl mt={4}>
              <FormLabel>Availability</FormLabel>
              <Select
                name="availability"
                value={newMenuItem.availability}
                onChange={handleChange}
              >
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </Select>
            </FormControl>
          </ModalBody>
          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleAddMenu}>
              Add
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Box>
  );
};

export default MenuPage;

