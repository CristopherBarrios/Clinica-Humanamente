import React from 'react'
import Emilio from '../estilo/images/Emilio.JPG'
import Maria from '../estilo/images/Maria.jpeg'
import Raul from '../estilo/images/Raul.jpg'
import Rolando from '../estilo/images/Rolando.jpeg'
import Vladimir from '../estilo/images/Vladimir.jpeg'
import Magnanimo from '../estilo/images/Magnanimo.jpeg'
import Diana from '../estilo/images/Diana.jpg'
import Cristina from '../estilo/images/Cristina.jpg'
import Gabriela from '../estilo/images/Gabriela.JPG'
import Shirley from '../estilo/images/Shirley.JPG'

import ContactoItem from './Contactoitem';

class Quiensomos extends React.Component{
    constructor(){
        super();
        this.state = {
            contactos: [{
                id: 1,
                foto: Emilio,
                nombre: 'Dr Emilio Quinto',
                desc: "Psiquiatra USAC y UFM\n" +
               "Maestría en terapia familiar y Logoterapia.\n" +
               "Terapeuta y supervisor certificado en terapia cognitiva conductual (ACT, USA)\n" +
               "Terapeuta y supervisor certificado en terapia de parejas e individual focalizada en las emociones (ICEEFT Canadá)\n" +
               "Entrenamiento en Psiquiatría Intervencionista (APA, USA)\n" +
               "Entrenamiento en trastornos de Alimentación (Renfrew Center, USA)\n" +
               "Diplomado en Medicina del sueño, (Universidad Francisco de Vitoria, Madrid)\n" +
               "Profesor Asociado Posgrado de Psiquiatría USAC  Guatemala  y posgrado de psiquiatría Universidad Nacional Autónoma de Honduras.\n" +
               "Profesor Asociado Psicologia UFM." 
                
            },
            {
                id: 2,
                foto: Maria,
                nombre: 'Dra María Renée Gándara',
                desc: "Psiquiatra\n" +
                "Entrenamiento en terapia de parejas focalizada en las emociones\n" +
                "Entrenamiento en Análisis Transaccional\n" +
                "Directora Maestría Psicología médica Integral UFM"
            },
            {
                id: 3,
                foto: Raul,
                nombre: 'Dr Raúl Higueros',
                desc: "Psiquiatra USAC\n" +
                "Especialización en Logoterapia\n" +
                "Entrenamiento en terapia cognitiva \n" +
                "Entrenamiento en Terapia de parejas Focalizada en las emociones \n" +
                "Maestría del Neurodesarrollo USAC\n" +
                "Diplomado en Medicina del sueño (Universidad Francisco de Vitoria, Madrid)\n" +
                "Profesor Asociado posgrado de Psiquiatría USAC."
                
            },
            {
                id: 4,
                foto: Rolando,
                nombre: 'Dr Rolando Lemus',
                desc: "Psiquiatra\n" +
                "Psicólogo clínico\n" +
                "Especialización Psiquiatría de niños y adolescentes (UNAM México)\n" +
                "Profesor asociado Psicologia USAC"
                
            },
            {
                id: 5,
                foto: Magnanimo,
                nombre: 'Dr Walter Rinze',
                desc: "Psiquiatra\n" +
                "Entrenamiento en Terapia Focalizada en las emociones \n" +
                "Profesor asociado posgrado de psiquiatría USAC"
                
            },
            {
                id: 6,
                foto: Vladimir,
                nombre: 'Dr Vladimir López',
                desc: "Psiquiatra\n" +
                "Psicólogo clínico\n" +
                "Entrenamiento en terapia focalizada en las emociones \n" +
                "Profesor asociado de psicología USAC"
                
            },

            {
                id: 7,
                foto: Shirley,
                nombre: 'Licenciada Shirley Galindo',
                desc: "Psiquiatra\n" +
                "Maestría en Terapia Familiar\n" +
                "Psicóloga Familiar\n" +
                "Psicóloga Organizacional\n" +
                "Terapeuta certificada terapia de parejas focalizada en las emociones (ICEEFT, Canadá)\n" +
                "Entrenamiento en terapia cognitiva conductual"
                
            },
            {
                id: 8,
                foto: '',
                nombre: 'Lic. Carmen Lucia Ramirez',
                desc: "Psicologia Clínica\n" +
                "Orientadora Familiar\n" +
                "Certificacada en Terapia Cognitivo Conductual\n" +
                "Certificada en Terapia  Focalizada en las Emociones\n" +
                "Catedrática Maestría en Psicología Médica Integral  UFM\n" +
                "Catedrática  E.F.C  Parroquia San Antonio Ma Claret\n" +
                "Coordinadora Investigación Clínica"
                
            },
            {
                id: 9,
                foto: Gabriela,
                nombre: 'Gabriela Estrada ',
                desc:
                "Licenciada en psicología clínica. \n" +
                "Certificación en psicotraumatologia CCPT- I y II por Institute Newman México.\n" + 
                "Certificación en psicoterapia cognitiva en víctimas de abuso sexual en adultos. Por centro de terapia cognitiva Balance Guatemala."
                
            },
            {
                id: 10,
                foto: Diana,
                nombre: 'Diana Carolina Cardona Gutiérrez ',
                desc: "Certificación en Psicotraumatologia CCTP-I y II por Newman Institute, México. \n" +
                "Entrenadora Certificada en Cuidador Competente en trauma por Back2Back, México. \n" +
                "Cursos de Terapia cognitiva: psicoterapia con víctimas de abuso sexual (adultos) y Terapia cognitiva enfocada en Trauma, por Clinica Balance.\n" +
                "Profesional nivel básico en prevención e intervención primaria en crisis ante la crisis suicida en niños/as y adolescentes, por CreSer Jugando, Costa Rica. \n" +
                "Diplomado en Desarrollo Integral de la niñez y adolescencia, por Centro Esdras. "
                
            },
            {
                id: 11,
                foto: Cristina,
                nombre: 'María Cristina Bolaños V.',
                desc: "Terapia individual dirigido a adultos jóvenes \n" +
                "Psicóloga Clínica\n" +
                "Postgrado en Análisis Existencial y Maestría en Logoterapia\n" +
                "Externship en TFE"
                
            },
        
        ]}}
    render(){
        var contactList = this.state.contactos.map(item => <ContactoItem key={item.id} item={item} desc={this.state.desc} />)

        return(              
        <div>
            <div style={{ marginTop: '3%', textAlign: "center", fontSize: '33px', color:'#016495'}}>Socios</div>
            {contactList}
        </div>

        )
    }
}
export default Quiensomos