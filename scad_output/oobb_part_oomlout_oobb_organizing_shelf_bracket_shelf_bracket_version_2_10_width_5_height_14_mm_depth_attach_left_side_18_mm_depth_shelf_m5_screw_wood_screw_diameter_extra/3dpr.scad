$fn = 50;


difference() {
	union() {
		translate(v = [0, 39.0000000000, 0]) {
			hull() {
				translate(v = [-69.5000000000, 11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [69.5000000000, 11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-69.5000000000, -11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [69.5000000000, -11.0000000000, 0]) {
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
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#cylinder(h = 250, r = 5.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.7500000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
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
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#cylinder(h = 250, r = 5.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.7500000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [52.5000000000, 46.5000000000, 14.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.3750000000, r2 = 4.5000000000);
						}
						#cylinder(h = 250, r = 4.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.3750000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-52.5000000000, 46.5000000000, 14.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.3750000000, r2 = 4.5000000000);
						}
						#cylinder(h = 250, r = 4.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.3750000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-74.5000000000, 37.5000000000, 0]) {
			cube(size = [149, 18, 11]);
		}
	}
}