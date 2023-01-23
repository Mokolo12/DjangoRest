import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';


const Menu = () => {
	@@ -8,10 +9,12 @@ const Menu = () => {
            <span className="ms-2 navbar-brand mb-0 h1">Menu</span>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div className="navbar-nav">
                    <Link to='/users' className="nav-item nav-link active">
                        List of all users
                    </Link>
                    <Link to='/projects' className="nav-item nav-link active">
                        List of all projects
                    </Link>
                </div>
            </div>
        </nav>