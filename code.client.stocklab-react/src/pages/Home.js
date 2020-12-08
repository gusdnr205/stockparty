import React, { Component } from "react";
import Slider from "react-slick";
import img1 from "../img/img1.jpeg";
import img2 from "../img/img2.jpeg";
import img3 from "../img/img3.jpeg";
import img4 from "../img/img4.jpeg";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Links from './link';

function SampleNextArrow(props) {
    const { className, style, onClick } = props;
    return (
      <div
        className={className}
        style={{ ...style, display: "block", background: "black", }}
        onClick={onClick}
      />
    );
  }
  
  function SamplePrevArrow(props) {
    const { className, style, onClick } = props;
    return (
      <div
        className={className}
        style={{ ...style, display: "block", background: "black" }}
        onClick={onClick}
      />
    );
  }

export default class page1 extends Component {
  render() {
    const settings = {
        slide: 'div',
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        autoplay:true,
        autoplaySpeed:3000,
        prevArrow : <SamplePrevArrow />,
        nextArrow : <SampleNextArrow />,
        dotsClass : "slick-dots"
    };
    return (
        <div style={{padding: "100px"}}>
            <hr style={{color: "#984b61" }} />
        <Slider {...settings} style={{padding:"100px"}}>
             <div>
                <img src={ img1 } title={img1} alt={img1} 
                    style={{width:"100%", height:"60vh"}}/>
            </div>
            <div>
                <img src={ img2 } title={img2} alt={img2} 
                    style={{width:"100%", height:"60vh"}}/>
            </div>
            <div>
                <img src={ img3 } title={img3} alt={img3} 
                    style={{width:"100%", height:"60vh"}}/>
            </div>
            <div>
                <img src={ img4 } title={img4} alt={img4} 
                    style={{width:"100%", height:"60vh"}}/>
            </div>
        </Slider>
        <Links />
        </div>
    );
  }
}

