import React from 'react'
import Emilio from '../estilo/images/Emilio.jpeg'
import Shirley from '../estilo/images/Shirley.jpeg'

class Contactanos extends React.Component{
    render(){
        return(              
        <div>
            <div className="GridCon">
                <img className='Perfil' src={Emilio} />

                <div>
                    <div style={{ fontSize: '25px', color:'#016495'}}>
                        <p>Dr. Emilio Quinto</p></div>

                    <div style={{fontSize: '20px', textAlign: 'justify'}}>
                        <p>Psiquiatra.</p>
                        <p>Maestria en terapia familiar y conyugal.</p>
                        <p>Terapeuta de parejas certificado por ICEEFT
                            Fellow de la American Academy of Psychiatry y World Psychiatric Association.</p>
                        <p>Catedratico universitario en Psicología y Psiquiatría.</p>
                    </div>
                </div>

            </div>

            <div className="GridCon" style={{marginBottom: '1%'}}>
                <img className='Perfil' src={Shirley} />
            
                <div>
                    <div style={{ fontSize: '25px', color:'#016495'}}>  
                        <p>M.A Shirley Galindo</p>
                    </div>

                    <div style={{fontSize: '20px', textAlign: 'justify'}}>
                        <p>Psicóloga Familiar.</p>
                        <p>Maestría en terapia familiar y conyugal.</p>
                        <p>especializada en  TFE y terapia cognitiva conductual.</p>
                        <p>Catedrática universitaria en psicología.</p>
                    </div>
                </div>

            </div>

         </div>

        )
    }
}
export default Contactanos