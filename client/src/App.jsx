import React, { useState } from 'react'
import {
  createBrowserRouter,
  RouterProvider,
  Outlet,
} from "react-router-dom";
import NavBar from "./NavBar.jsx"
import Squads from "./Squads.jsx"
import Create from "./Create.jsx"
import Home from "./Home.jsx"
import './App.css'

const Dashboard = () => {
  return (
    <div>
      <NavBar />
      <hr/>
      <Outlet />
    </div>
  )
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard />,
    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/squads",
        element: <Squads />,
      },
      {
        path: "/create",
        element: <Create />,
      },
      
    ]
  },
])

function App() {
  return (
    <div>
      <RouterProvider router={router} />
   </div>


 
  );
}

export default App;
