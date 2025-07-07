$fn = 50;


difference() {
	union() {
		translate(v = [0, 30.0000000000, 0]) {
			hull() {
				translate(v = [-69.5000000000, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [69.5000000000, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-69.5000000000, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [69.5000000000, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
		translate(v = [-67.5000000000, 0, 0]) {
			hull() {
				translate(v = [-2.0000000000, 32.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [2.0000000000, 32.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-2.0000000000, -32.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [2.0000000000, -32.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
		rotate(a = [0, 0, 23.9624889746]) {
			hull() {
				translate(v = [-73.3664335135, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [73.3664335135, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-73.3664335135, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [73.3664335135, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-60.5000000000, -30.0000000000, 7.0000000000]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 250, r = 3.6000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.8000000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-60.5000000000, 15.0000000000, 7.0000000000]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 250, r = 3.6000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.8000000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		#translate(v = [-7.5000000000, 37.5000000000, 7.0000000000]) {
			rotate(a = [0, 90, -90]) {
				cylinder(h = 30, r = 3.2500000000);
			}
		}
		#translate(v = [-52.5000000000, 37.5000000000, 7.0000000000]) {
			rotate(a = [0, 90, -90]) {
				cylinder(h = 30, r = 3.2500000000);
			}
		}
	}
}