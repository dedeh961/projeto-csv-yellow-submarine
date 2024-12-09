import React, { useState, useEffect } from "react";
import {
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    CircularProgress
} from "@mui/material";

const listarCSVs = () => {
    const [listaCSVs, definirLista] = useState([]);
    const [carregando, definirCarregando] = useState(true);
    const url = "http://localhost:5000/ListarCSVs";

    useEffect(() => {
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

        recuperarLista();
    }, []);

    const cabecalho = () => {
        return (
            <TableHead>
                <TableRow>
                    <TableCell>ID</TableCell>
                    <TableCell>Nome</TableCell>
                    <TableCell>URL</TableCell>
                </TableRow>
            </TableHead>
        );
    }

    const linhas = () => {
        return (
            <TableBody>
                {listaCSVs.map((linha) => (
                    <TableRow key={linha.id}>
                        <TableCell>{linha.id}</TableCell>
                        <TableCell>{linha.nome}</TableCell>
                        <TableCell>{linha.url}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        );
    }

    if (carregando) {
        return <CircularProgress />;
    }

    return (
        <TableContainer component={Paper}>
            <Table>
                {cabecalho()}
                {linhas()}
            </Table>
        </TableContainer>
    );
};

export default listarCSVs;
