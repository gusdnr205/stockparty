import React, { Component } from 'react';
import './Menubar.css';
import './MainDiv.css';
import MainDiv from './MainDiv';
import './Menubar.css';
import stocklab from './stocklab.png';
import { Home, page1, page2, page3 } from './pages';
import { CodeInfo} from './pages';
import { Link, Route, BrowserRouter as Router } from "react-router-dom";
import Footer from './footer';

class Menubar extends Component {
    render(){
      return (
        <div>
        <img src={ stocklab } alt="stocklab" className="i" />
          <Router>
            <div>
              <nav id="menubar">
                <ul>
                    <li><Link to='/' className='link'>Home</Link></li>
                    <li><Link to="/page1" className='link'>Index</Link></li>
                    <li><Link to="/page2" className='link'>TrendTable</Link></li>
                    <li><Link to="/page3" className='link'>Chart</Link></li>
                </ul>
              </nav>
              
              <Route exact path='/' component={Home} />
              <Route path='/page1' component={page1} />
              <Route path='/page2' component={page2} />
              <Route path='/page3' component={page3} />
            </div>  
          </Router>
          <Footer/>
        </div>
      );
    }
  }

  
  
  export default Menubar;
  

