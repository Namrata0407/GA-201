import React from 'react';
import {Routes,Route} from "react-router-dom";
import HomePage from './HomePage';
import MenuPage from './MenuPage';
import TakeOrdersPage from './TakeOrdersPage';
import OrderPage from './OrderPage';
import ExitPage from './ExitPage';



const AllRoutes = () => {
  return (
    <Routes>
     
 
     <Route path="/" element={<HomePage/>} />;
        <Route path="/menu" element={<MenuPage/>} />
        <Route path="/take-orders" element={<TakeOrdersPage/>} />
        <Route path="/orders" element={<OrderPage/>} />
        <Route path="/exit" element={<ExitPage/>} />
   
        </Routes>
  );
};

export default AllRoutes;
