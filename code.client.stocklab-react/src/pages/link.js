import React, { Component } from "react";
import { Link } from 'react-router-dom';
import Iframe from 'react-iframe';

const Links = () => {
    return (
        <div style={{padding:"100px"}}>
        <Iframe url="https://finance.naver.com/news/"
        width="100%"
        height="1000px"
        id="myId"
        className="myClassname"
        display="initial"
        position="relative"/>
        </div>
    );
};

export default Links;

