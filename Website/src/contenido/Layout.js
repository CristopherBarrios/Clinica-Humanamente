import React from 'react'
import '../estilo/style.css'
import Clinica from '../estilo/images/clinica.jpg'
import Prueba from './Prueba'
import Home from './Home'
import Contactanos from './Contactanos'
import {Route, BrowserRouter as Router, Link} from 'react-router-dom'
import Quiensomos from './Quiensomos'
class Layout extends React.Component{
    constructor(){
        super();
        this.state = {
            page: 1
        }
    }
    switchp(num){
        var curp = this.state.page;
        var bttn = document.getElementById('l' + curp);
        var bttn2 = document.getElementById('l' + num);
        bttn.classList.toggle('ac');
        bttn2.classList.toggle('ac');
        this.setState({page: num});
    }

    render(){
        return(

            <Router>
                
                <div style={{height: '15%', width: '100%', backgroundColor: '#018acc'}}>
                        <img className='headr' src={Clinica} />
                </div>
                <div style={{height: '5%', width: "100%", backgroundColor: '#07a6f3'}}>
                    <div className="nav">
                        <Link id='l1' onClick={() => {this.switchp(1)}} className="navb ac" to='/'>
                            HOME
                        </Link>
                        <Link id='l3' onClick={() => {this.switchp(3)}} className="navb" to='/quiensomos'>
                        QUIENES SOMOS
                        </Link>
                        <Link id='l4' onClick={() => {this.switchp(4)}} className="navb" to='/Contactanos'>
                        CONTACTANOS
                        </Link>
                        <Link id='l2' onClick={() => {this.switchp(2)}} className="navb" to='/prueba-depresion'>
                        SERVICIOS
                        </Link>
                    </div>
                </div>
                <div>
                    <Route path='/' exact render={(props) => <Home {...props}/>} />
                    <Route path='/quiensomos' exact render={(props) => <Quiensomos {...props}/>} />
                    <Route path='/prueba-depresion' exact render={(props) => <Prueba {...props}/>} />
                    <Route path='/Contactanos' exact render={(props) => <Contactanos {...props}/>} />
                </div>

                <div className='footr'>
                    Clinica Humanamente ©
                </div>
            </Router>
        )
    }
}
export default Layout