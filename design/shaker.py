import cadquery as cq

# Parameters (easy to change on your phone)
hub_diameter = 40.0
hub_height = 15.0
axle_hole = 8.2  # 8mm axle + 0.2mm tolerance for 3D printing
set_screw_hole = 3.0

# 1. Create the main hub
hub = (
    cq.Workplane("XY")
    .circle(hub_diameter / 2)
    .extrude(hub_height)
)

# 2. Add the center axle hole
hub = hub.faces(">Z").workplane().hole(axle_hole)

# 3. Add a side hole for a set-screw (m3)
hub = (
    hub.faces("<X") # Select a side face
    .workplane(offset=-hub_height/2, centerOption="CenterOfMass")
    .hole(set_screw_hole)
)

# CRITICAL: Export for GitHub to find
if __name__ == "__main__":
    cq.exporters.export(hub, "star_wheel_hub.stl")

