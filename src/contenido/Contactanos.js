import React from 'react'
import Clinica from '../estilo/images/clinica.jpg'
import Reloj from '../estilo/images/reloj.png'
import Location from '../estilo/images/location.png'
import Llamada from '../estilo/images/llamada.png'
import Mail from '../estilo/images/mail.png'

class Contactanos extends React.Component{
    render(){
        return(              
            <div>
                <div className='Gridh' style={{marginTop: '0%', height:'73%'}}>
                    <div style={{height: '100%', width: '75%'}}>
                        <img style={{height: '40%', width: '100%', marginTop: '70%', marginLeft: '1%'}} src={Clinica} />
                    </div>
                    <div>
                        <div style={{marginTop: '4%', marginLeft: '25%', fontSize: '28px', textAlign: 'justify', color:'#016495'}}>
                            <p style={{marginLeft: '10%'}}>Clinica Humanamente</p>
                            <p>“Bienestar y confianza humanamente”</p>
                        </div>

                        <div className='Gridh' style={{fontSize: '19px', fontWeight: 'bold'}}>
                            <img src={Llamada} style={{marginTop: '15%', marginLeft: '50%',height: '40%', width: '23%'}} />
                            <div>
                                <p>(502) 2369-3238</p>
                                <p>(502) 2369-0709</p>
                                <p>(502) 2221-7449</p>
                            </div>
                            <img src={Mail} style={{marginLeft: '50%',height: '100%', width: '20%'}}/>
                            <p>informacion@clinicahumanamente.com</p>
                            <img src={Location} style={{marginLeft: '50%',height: '100%', width: '20%'}}/>
                            <p>Visitenos en: 20 av "A" 0-49 zona 15 Vista Hermosa II</p>
                            <img src={Reloj} style={{marginTop: '20%', marginLeft: '50%', height: '35%', width: '25%'}}/>
                            <div>
                                <p>Horario entre semana:</p>
                                <p>Lunes a viernes 8:00 AM - 5:00 PM</p>
                                <p>Sabado 8:00 AM - 12:00 PM</p>
                                <p>Domingo - CERRADO</p>
                            </div>
                        </div>
                    </div>
                </div>   

            </div>

        )
    }
}
export default Contactanos