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
                    <TableCell sx={{ backgroundColor: 'gray', color: 'white' }}>ID</TableCell>
                    <TableCell sx={{ backgroundColor: 'gray', color: 'white' }}>Nome</TableCell>
                    <TableCell sx={{ backgroundColor: 'gray', color: 'white' }}>URL</TableCell>
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
        <TableContainer component={Paper} style={{ width: '75%', margin: '20px auto' }}>
            <Table>
                {cabecalho()}
                {linhas()}
            </Table>
        </TableContainer>
    );
};

export default listarCSVs;
