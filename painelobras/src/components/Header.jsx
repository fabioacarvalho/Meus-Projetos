import './Header.css'
import React from "react";

const Header = props => {
    return (
        <div className="Nav">
            <nav>
                <h1><a href="/">Logo</a></h1>
                <div>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/">About</a></li>
                        <li><a href="/">Contact</a></li>
                        
                    </ul>
                </div>
            </nav>
        </div>
    )
}

export default Header