import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Link } from "react-router-dom";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="home">
			 <div>
				<h1>
					Welcome to the Star Wars Project
				</h1>
			 </div>
			 <div className="buttons">
				<Link to={'/signup'}>
					<button>Sign Up</button>
				</Link>
					<button>Log In</button>
			</div>
		</div>
	);
};
