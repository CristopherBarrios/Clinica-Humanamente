import React from 'react'
import '../estilo/style.css'
import Prueba from './Prueba'
import Home from './Home'
import Contactanos from './Contactanos'
import {Route, BrowserRouter as Router, Link} from 'react-router-dom'
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
                        <img style={{height: '90%', width: '10%', marginTop: '0.5%', marginLeft: '5%', borderRadius: '10px'}} src='https://scontent-mia3-2.xx.fbcdn.net/v/t1.0-9/83970114_1900671686731220_1765311045615747072_n.jpg?_nc_cat=109&_nc_sid=09cbfe&_nc_ohc=Nptr6hJ7sRoAX8mocxn&_nc_ht=scontent-mia3-2.xx&oh=9e19e305ff18d59bef2120577601b44c&oe=5F5EC55A' />
                </div>
                <div style={{height: '5%', width: "100%", backgroundColor: '#07a6f3'}}>
                    <div className="nav">
                        <Link id='l1' onClick={() => {this.switchp(1)}} className="navb ac" to='/'>
                            HOME
                        </Link>
                        <Link id='l2' onClick={() => {this.switchp(2)}} className="navb" to='/'>
                        SERVICIOS
                        </Link>
                        <Link id='l3' onClick={() => {this.switchp(3)}} className="navb" to='/prueba-depresion'>
                        PRUEBAS
                        </Link>
                        <Link id='l4' onClick={() => {this.switchp(4)}} className="navb" to='/Contactanos'>
                        CONTACTANOS
                        </Link>
                    </div>
                </div>
                <div>
                    <Route path='/' exact render={(props) => <Home {...props}/>} />
                    <Route path='/prueba-depresion' exact render={(props) => <Prueba {...props}/>} />
                    <Route path='/Contactanos' exact render={(props) => <Contactanos {...props}/>} />
                </div>

                <div style={{ paddingTop: '1%', color: '#014e73', fontSize: '22px', paddingLeft: '2%', backgroundColor: '#07a6f3', position: "relative", height: '5%', width: '98%', bottom: '0'}}>
                    Clinica Humanamente ©
                </div>
            </Router>
        )
    }
}
export default Layout