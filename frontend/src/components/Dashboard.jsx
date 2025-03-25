import React, { useEffect, useState } from "react";
import axios from "axios";
import API_BASE_URL from "../config";
import {
  Container, Grid, Card, CardContent, Typography, Select, MenuItem, useMediaQuery
} from "@mui/material";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import { motion } from "framer-motion";

const Dashboard = () => {
  const [data, setData] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState("");
  const isMobile = useMediaQuery("(max-width: 600px)"); // Detects if on mobile

  useEffect(() => {
    axios.get(`${API_BASE_URL}data/`)
      .then(response => setData(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  const filteredData = selectedCountry
    ? data.filter(item => item.country === selectedCountry)
    : data;

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" align="center" sx={{ fontWeight: "bold", color: "#333", mb: 4 }}>
        📊 Data Visualization Dashboard
      </Typography>

      {/* Filters Section */}
      <Grid container spacing={2} justifyContent="center">
        <Grid item xs={12} sm={6} md={4}>
          <Select
            fullWidth
            displayEmpty
            value={selectedCountry}
            onChange={(e) => setSelectedCountry(e.target.value)}
          >
            <MenuItem value="">🌍 Select Country</MenuItem>
            {[...new Set(data.map(d => d.country))].map((country, index) => (
              <MenuItem key={index} value={country}>{country}</MenuItem>
            ))}
          </Select>
        </Grid>
      </Grid>

      {/* Charts and Stats Section */}
      <Grid container spacing={3} sx={{ mt: 3 }}>
        {/* Chart Section */}
        <Grid item xs={12} md={8}>
          <motion.div whileHover={{ scale: 1.05 }} transition={{ duration: 0.3 }}>
            <Card sx={{ boxShadow: 3, backgroundColor: "#fafafa" }}>
              <CardContent>
                <Typography variant="h6" sx={{ mb: 2 }}>📉 Intensity & Relevance by Country</Typography>
                <ResponsiveContainer width="100%" height={isMobile ? 250 : 300}>
                  <BarChart data={filteredData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="country" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="intensity" fill="#1976D2" />
                    <Bar dataKey="relevance" fill="#E91E63" />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </motion.div>
        </Grid>

        {/* Statistics Section */}
        <Grid item xs={12} md={4}>
          <motion.div whileHover={{ scale: 1.05 }} transition={{ duration: 0.3 }}>
            <Card sx={{ boxShadow: 3, backgroundColor: "#E3F2FD", textAlign: "center", p: 2 }}>
              <Typography variant="h6">🌍 Total Countries</Typography>
              <Typography variant="h4">{new Set(data.map(d => d.country)).size || 0}</Typography>
            </Card>
          </motion.div>

          <motion.div whileHover={{ scale: 1.05 }} transition={{ duration: 0.3 }} style={{ marginTop: 16 }}>
            <Card sx={{ boxShadow: 3, backgroundColor: "#FDEDEC", textAlign: "center", p: 2 }}>
              <Typography variant="h6">🔎 Total Topics</Typography>
              <Typography variant="h4">{new Set(data.map(d => d.topic)).size || 0}</Typography>
            </Card>
          </motion.div>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
