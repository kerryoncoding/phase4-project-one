import React from "react"
import { NavLink } from "react-router-dom"

function NavBar(){
   return (
      <nav>
         <NavLink exact to="/Squads" > SHOW SQUADS </NavLink>
         <NavLink exact to="/create" > CREATE SQUAD </NavLink>
         <NavLink exact to="/" > LOG OUT </NavLink>
      </nav>
   )
}

export default NavBar;
