import React from 'react'
import './AboutUs.css'
import Logo from '../assets/gcc.png'
import {Link } from "react-router-dom";

function AboutUs() {

  return (
    <div>
        <div className='nav__cont'>
            <div className='logo__cont'>
              <Link to='/'>
              <img src={Logo} alt='' className='logo'/>
              </Link>
            </div>
            <div className='links__cont'>
              <div>
                  <Link to='/about' style={{textDecoration:'none'}}>
                      <h5>About</h5>
                  </Link>
              </div>
              <div>
                  <Link to='/sermons' style={{textDecoration:'none'}}>
                      <h5>Sermons</h5>
                  </Link>
              </div>
              <div>
                  <Link to='/merchandise' style={{textDecoration:'none'}}>
                      <h5>Merchandise</h5>
                  </Link>
              </div>
              <div>
                  <Link to='/connect' style={{textDecoration:'none'}}>
                      <h5>Connect</h5>
                  </Link>
              </div>
            </div>
        </div>
        <div className='about__us__cont'>
          <div className='car__cont'> 
            {/* //swiper js space */}
          </div>
          <div className='about__body__cont'>
            <div className='info__cards'>
              <h1>Vission.</h1>
              <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
              </p>
            </div>
            <div className='info__cards'>
              <h1>Mission.</h1>
              <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
              </p>
            </div>
          </div>
        </div>      
    </div>
  )
}

export default AboutUs