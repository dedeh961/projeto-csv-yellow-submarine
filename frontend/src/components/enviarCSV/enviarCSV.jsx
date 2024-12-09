import { FilePond, registerPlugin } from 'react-filepond';
import 'filepond/dist/filepond.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import style from './enviarCSV.module.css';


registerPlugin(FilePondPluginFileValidateType);

const enviarCSV = () => {
  return (
    <div>
      <FilePond
        className={style["drop-area"]}
        allowMultiple={false}
        acceptedFileTypes={['text/csv']}
        labelIdle="Arraste ou clique aqui para selecionar um arquivo CSV"
        instantUpload={false} // Desabilita o envio automático
        server={{
          url: 'http://localhost:5000/EnviarCSV',
        }}
      />
    </div>
  );
};

export default enviarCSV;
