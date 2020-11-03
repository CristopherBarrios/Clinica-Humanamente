import {shallow} from 'enzyme';
import Prueba from './Prueba';
import Prueba from './Home';
import Prueba from './Contactanos';

describe('<Prueba>', () => {
    it('Hace render la prueba de ansiedad y depresion', () => {
        const prueb = shallow(<Prueba />);
        expect(prueb.find('input').length).toEqual(4);
    });

    it('Hace render la pagina inicial', () => {
        const prueb = shallow(<Prueba />);
        expect(prueb.find('textarea').length).toEqual(1);
    });

    it('Hace render la pagina de contactanos', () => {
        const prueb = shallow(<Prueba />);
        expect(prueb.find('textarea').length).toEqual(1);
    });
}