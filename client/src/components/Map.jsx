export default function Map( { level, mapTiles, onTileClick }) {
    // Import all tile images and assign them to a hash
    const tileImages = import.meta.glob(
        "../assets/map_tiles/*.png",
        { eager: true, import: "default" }
    )

    class Map{
        constructor(width, height, tiles) {
            this.width = width
            this.height = height
            this.tiles = tiles
        }
    }

    const map = new Map(mapTiles.width, mapTiles.height, mapTiles.tiles)

    return (
        <div style={{display:"flex",justifyContent:"center", margin:"1em 0em"}}>
            {map && (
            <div className="grid" style={{ "--gridWidth": map.width, "--gridHeight": map.height, width: "40vw", maxWidth: "100%",}}>
                {map.tiles.map((tile, i) => {
                    const tileSrc = tileImages[`../assets/map_tiles/${tile.number}.png`]
                    return <div key={i} id={tile.number} className={`cell ${tile.number !== 0 ? "hoverable" : ""}`} style={{ background: `url(${tileSrc})`, transform: `rotate(${tile.rotation}deg)`, backgroundSize: "contain", backgroundRepeat: "no-repeat", backgroundPosition: "center"}} onClick={() => onTileClick(tile)}/>
            })}
            </div>
            )}
        </div>
    )
}