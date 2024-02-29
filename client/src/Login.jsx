import React, { UseState } from 'react'
import { useHistory } from 'react-router-dom'
import { useFormik } from 'formik'


function Login() {
   const [signUp, setSignUp] = useState(false)
   const history = useHistory()

   const handleClick = () => setSignUp(signUp) => !signUp)
   
   return (
      <div className="about-container">
         <h2>Welcome to Pod Squad!</h2>
         <h3>Please Login</h3>
         <button onClick={handleClick}>{signUp ? 'Log In!' : 'Register now!'}</button>
         <Form onSubmit={console.log}>
         <lable>Username</lable>
         <input type='text' name='name' value={'value'} onChange={console.log} />
            {signUp && (
               <>
                  <label>Email</label>
                  <input type='text' name='email' value={'value'} onChange={console.log} />
               </>
            )}
            <input type='submit' value={signUp?'Sign Up!':'Log In!'} />
         </Form>
      </div>
   )
}



export default Login;