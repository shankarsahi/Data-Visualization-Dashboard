import React from "react";
import { AppBar, Toolbar, Typography, IconButton } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import { motion } from "framer-motion";

const Navigation = () => {
  return (
    <motion.div initial={{ y: -50 }} animate={{ y: 0 }} transition={{ duration: 0.5 }}>
      <AppBar position="static" sx={{ backgroundColor: "#1E1E2D" }}>
        <Toolbar>
          {/* <IconButton edge="start" color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton> */}
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            📊 Data Dashboard
          </Typography>
        </Toolbar>
      </AppBar>
    </motion.div>
  );
};

export default Navigation;
