import SalvarCSV from "./components/salvarCSV/salvarCSV";
import ListarCSVs from "./components/listarCSVs/listarCSVs";
import { useState, useEffect } from "react";

function App() {
  const [listaCSVs, definirLista] = useState([]);
  const [carregando, definirCarregando] = useState(true);
  const url = "http://localhost:5000/ListarCSVs";

  const recuperarLista = async () => {
    try {
      const resposta = await fetch(url);
      const resultado = await resposta.json();
      definirLista(resultado['links']);
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
    } finally {
      definirCarregando(false);
    }
  };

  useEffect(() => {
    recuperarLista();
  }, []);

  return (
    <>
      <SalvarCSV eventoArquivoSalvo={recuperarLista}/>
      <ListarCSVs listaCSVs={listaCSVs} carregando={carregando} />
    </>
  )
}

export default App;
