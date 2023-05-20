import React from 'react';
import '../styles/WelcomePage.scss';

const WelcomePage = () => {
  return (
    <div className="welcome-page">
        <div className="wrapper">
            <h1 className="heading">GRANGER</h1>
            <h2 className="sub-heading">Bard Powered AI ChatBot</h2>
            <div className="buttons">
                <a href="/login" className="button1">Login</a>
                <a href="/login" className="button2">Sign Up</a>
            </div>
        </div>
      <p className="welcome-page__copy-right"></p>
    </div>
  );
};

export default WelcomePage;