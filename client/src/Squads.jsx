import React from "react"

// function SquadList() {
//    const [squad, setSquad] = useState([]);

//    useEffect(() => {
//       fetch("http://localhost/squads")
//         .then((r) => r.json())
//         .then((squad) => setSquad(squad));
//     }, []);


function Squads(){
   return (
      <div className="about-container">
         <h2>Squads</h2>
         {/* <section>
            {squad.map((suqad) => (
               <SquadItem key={squad.id} squad={squad} />
            ))}
         </section> */}
         <p>I have a strong background in mechanical engineering and have been developing consumer, industrial and medical products for over 15 years.  I have touched on all aspects of product development from initial concept through to manufacturing. I love to see a design evolve into a product. A few examples of what I have worked on are shown on the Projects page.</p>
         <div className="skill-list">
            <h3>Skills:</h3>
            <ul>
               <li>
                  3D CAD tools (SolidWorks)
               </li>
               <li>
                  Design For Manufacture & Assembly
               </li>
               <li>
                  Rapid Prototyping
               </li>
            </ul>
         </div>
      </div>
      
   )
}

export default Squads;