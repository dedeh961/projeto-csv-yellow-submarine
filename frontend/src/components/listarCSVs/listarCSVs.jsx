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

const listarCSVs = ({ listaCSVs, carregando }) => {
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
