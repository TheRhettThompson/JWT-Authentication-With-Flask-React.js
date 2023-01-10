import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/index.css";
import { Link } from "react-router-dom";
 

export const Login = () => {
	const { store, actions} = useContext(Context);
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	//create a "check" so if they have a login, they will go to Dashboard page

 
	//create State for email and password

	return (
		<div>
			<div className="signup-form">
				<div className="forms">
				<label>Email Address</label>
				<input
				type="email"
				value={email}
				placeholder="Enter your email"
				onChange={e => setEmail(e.target.value)}
				/>
				</div>

				<div className="forms">
				<label>Password</label>
				<input
				type="password"
				value={password}
				placeholder="Enter your password"
				onChange={e => setPassword(e.target.value)}
				/>
				</div>
			</div>

			<div>
				<Link to= "/private">
					<button onClick={() =>actions.sign_up(email, password)} className= "btn btn-primary">
						Submit
					</button>
				</Link>
			</div>
		</div>

		//create button to send data to endpoint (user information)

	);
};
