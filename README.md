# Titan96  

![Titan96 render](images/Case_2025-Apr-16_09-12-48PM-000_CustomizedView3673466802.png)

**Titan96** is a compact 96% low-profile mechanical keyboard designed with sleek aesthetic. Powered by **KMK firmware** and built around the **Orpheus Pico microcontroller** by Hack Club.  

## Features  
- **96% Layout** – Compact yet functional, with all essential keys in a dense layout.  
- **Low-Profile Design** – Slimmer keys and case for a modern, ergonomic feel.  
- **KMK Firmware** – Highly customizable keymaps and macros using CircuitPython.  
- **Orpheus Pico MCU** – A powerful and open-source microcontroller by Hack Club.  
- **100 Keys** – Full numpad and navigation keys.  

## Parts
### CAD
![alt text](<images/Screenshot 2025-04-15 094616.png>)

### Schematic
![alt text](<images/Screenshot 2025-04-15 095241.png>)

### PCB
![alt text](<images/Screenshot 2025-04-15 095313.png>)

## Firmware & Software  
The Titan96 runs on **KMK**, a Python-based keyboard firmware for CircuitPython-compatible microcontrollers.  

### Setup Instructions  
1. **Flash CircuitPython** onto the Orpheus Pico.  
2. **Install KMK firmware** by copying the KMK files to the microcontroller.  
3. **Configure keymap** by editing `code.py` to match your layout.  
4. **Customize macros, layers, and RGB** (if supported) via KMK.  

For detailed KMK setup, refer to the [official KMK documentation](https://github.com/KMKfw/kmk_firmware).  

## Bill of Materials (BOM)  
| Part | Quantity | Price | Link | Notes |  
|------|----------|-------|------|-------|  
| Orpheus Pico MCU | 1 | N/A | N/A | Microcontroller by Hack Club |  
| Low-profile mechanical switches | 100 | $40.07 | [AliExpress](https://www.aliexpress.com/item/1005004620638633.html?spm=a2g0o.cart.0.0.422438daRMYwqx&mp=1&pdp_npi=5%40dis%21USD%21USD%2038.00%21USD%2034.20%21%21USD%2034.20%21%21%21%40211b65de17522704719968508eea63%2112000029862619758%21ct%21CM%216291529643%21%211%210) | Gateron Low-Profile |  
| Keycaps | 100 | $22.14 | [AliExpress](https://www.aliexpress.com/item/1005007074678857.html?spm=a2g0o.cart.0.0.422438daRMYwqx&mp=1&pdp_npi=5%40dis%21USD%21USD%2018.72%21USD%2014.98%21%21USD%2014.98%21%21%21%40211b65de17522704719968508eea63%2112000043563688519%21ct%21CM%216291529643%21%211%210) | MX stems |  
| PCB | 1 | N/A |  N/A | Custom Titan96 PCB |  
| Plate | 1 |  N/A | N/A |3D printed |  
| Case | 1 | N/A | N/A | 3D printed |  
| Diodes | 100 | $4.7 | [AliExpress](https://www.aliexpress.com/item/1005004333197874.html?spm=a2g0o.cart.0.0.422438daRMYwqx&mp=1&pdp_npi=5%40dis%21USD%21USD%200.33%21USD%200.31%21%21USD%200.31%21%21%21%40211b65de17522704719968508eea63%2112000028793174971%21ct%21CM%216291529643%21%211%210) | 1N4148 |  
| Stabilizers | 2u x 5, 6.5u x 1 | $15.58 | [AliExpress](https://www.aliexpress.com/item/1005005296240590.html?spm=a2g0o.cart.0.0.422438daRMYwqx&mp=1&pdp_npi=5%40dis%21USD%21USD%2011.59%21USD%2011.59%21%21USD%2011.59%21%21%21%40211b65de17522704719968508eea63%2112000032530884498%21ct%21CM%216291529643%21%211%210) | For larger keys (spacebar, Enter, etc.) |  
| OLED Screen 128 x 32 | 1 | $5.36 | [AliExpress](https://www.aliexpress.com/item/1005008670382155.html?spm=a2g0o.cart.0.0.422438daRMYwqx&mp=1&pdp_npi=5%40dis%21USD%21USD%201.63%21USD%201.14%21%21USD%201.14%21%21%21%40211b65de17522704719968508eea63%2112000046171658344%21ct%21CM%216291529643%21%211%210) | Screen |  
| M2 screws | 5 | $4.8 | [AliExpress](https://www.aliexpress.com/item/1005004533251852.html?spm=a2g0o.cart.0.0.286f38dacsLKbg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.55%21USD%201.32%21%21USD%201.32%21%21%21%40211b618e17522580510792994e43dd%2112000029523312277%21ct%21CM%216291529643%21%211%210) | To screw the plate into the case |
| M2 threaded inserts | 5 | $5.87 | [AliExpress](https://www.aliexpress.com/item/1005003582355741.html?spm=a2g0o.cart.0.0.286f38dacsLKbg&mp=1&pdp_npi=5%40dis%21USD%21USD%201.69%21USD%200.52%21%21USD%200.52%21%21%21%40211b618e17522580510792994e43dd%2112000026370649721%21ct%21CM%216291529643%21%211%210) | To screw the plate into the case |
 
*NB: All these prices include shipping to Cameroon*

Total : $98.52
## License  
This project is open-source under the **MIT License**.  

## Extra Renders
![3D Model above](<images/Screenshot 2025-04-15 094645.png>)
![3D Model below](<images/Screenshot 2025-04-15 094707.png>)
![Full render](<images/Case v12.png>)
![PCB with Silkscreen Art](<images/Screenshot 2025-04-15 095326.png>)