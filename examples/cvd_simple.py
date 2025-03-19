import viennals2d as vls
import viennaps2d as vps

def print_levelsets(domain, prefix="cvd_"):
    levelsets = domain.getLevelSets()
    for i, ls in enumerate(levelsets):
        mesh = vls.lsMesh()
        vls.lsToSurfaceMesh(ls, mesh).apply()
        vls.lsVTKWriter(mesh, prefix + str(i) + ".vtp").apply()

vps.Logger.setLogLevel(vps.LogLevel.WARNING)

domain = vps.Domain()
vps.MakeTrench(domain=domain, gridDelta=2.5, xExtent=80., yExtent=0., trenchWidth=30., trenchDepth=50., taperingAngle=5., material=vps.Material.Si).apply() 
domain.saveVolumeMesh("initial")

domain.duplicateTopLevelSet(vps.Material.SiO2)

iso = vps.IsotropicProcess(1.)
vps.Process(domain, iso, 10.).apply()
domain.saveVolumeMesh("final")

print_levelsets(domain)

# Access the level set object
ls_substrate = domain.getLevelSets()[0]
ls_deposited = domain.getLevelSets()[1]

# Generate surface meshes
mesh_substrate = vls.lsMesh()
vls.lsToSurfaceMesh(ls_substrate, mesh_substrate).apply()

mesh_deposited = vls.lsMesh()
vls.lsToSurfaceMesh(ls_deposited, mesh_deposited).apply()