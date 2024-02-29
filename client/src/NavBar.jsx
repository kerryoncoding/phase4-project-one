import React from "react"
import { NavLink } from "react-router-dom"

function NavBar(){
   return (
      <nav>
         <NavLink exact to="/" > HOME </NavLink>
         <NavLink exact to="/squads" > YOUR SQUADS </NavLink>
         <NavLink exact to="/create" > CREATE SQUAD </NavLink>
      </nav>
   )
}

export default NavBar;
